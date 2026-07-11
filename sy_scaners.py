from scapy.all import IP, TCP, sr1
from datetime import datetime
from pathlib import Path

# الأجهزة المصرح بفحصها
with open("target.txt", "r") as file:
    targets = [
        line.strip()
        for line in file
        if line.strip()
    ]
# المنافذ المراد فحصها
ports = [
    22,
    80,
    443,
    445,
    3389
]

# مكان حفظ التقرير
desktop_path = Path("/home/mohammad/Desktop")

# اسم التقرير
report_file = desktop_path / (
    f"syn_scan_report_"
    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
)

print("\nStarting SYN Scan...\n")

with open(report_file, "w") as report:

    report.write("=" * 50 + "\n")
    report.write("SYN PORT SCANNER REPORT\n")
    report.write(
        f"Date: {datetime.now()}\n"
    )
    report.write("=" * 50 + "\n\n")

    for target in targets:

        print(f"Scanning {target}\n")

        report.write(f"Target: {target}\n")
        report.write("-" * 30 + "\n")

        for port in ports:

            packet = IP(dst=target) / TCP(
                dport=port,
                flags="S"
            )

            response = sr1(
                packet,
                timeout=1,
                verbose=0
            )

            if response is None:
                status = "FILTERED"

            elif response.haslayer(TCP):

                tcp_flags = response[TCP].flags

                if tcp_flags == 0x12:
                    status = "OPEN"

                elif tcp_flags == 0x14:
                    status = "CLOSED"

                else:
                    status = f"UNKNOWN ({tcp_flags})"

            else:
                status = "UNKNOWN"

            print(f"Port {port:<5} -> {status}")

            report.write(
                f"Port {port:<5} -> {status}\n"
            )

        report.write("\n")

print("\nScan completed successfully.")
print(f"Report saved to:\n{report_file}")
