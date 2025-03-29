import re
import requests

# M3U 直播源 URL 列表
M3U_URLS = [
    "https://example.com/playlist1.m3u",
    "https://example.com/playlist2.m3u"
]

# 正则表达式匹配域名和 IP 地址
DOMAIN_PATTERN = re.compile(r"https?://([^:/\s]+)")
IP_PATTERN = re.compile(r"https?://(\d+\.\d+\.\d+\.\d+)")

domains = set()
ips = set()

# 解析 M3U 文件
for url in M3U_URLS:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        lines = response.text.split("\n")

        for line in lines:
            match_domain = DOMAIN_PATTERN.search(line)
            match_ip = IP_PATTERN.search(line)
            
            if match_domain:
                domains.add(match_domain.group(1))
            if match_ip:
                ips.add(match_ip.group(1))

    except Exception as e:
        print(f"⚠️  无法获取 {url}: {e}")

# 生成 YAML 文件
def save_yaml(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("payload:\n")
        for item in sorted(data):
            f.write(f"  - '{item}'\n")

save_yaml("domains.yml", domains)
save_yaml("ips.yml", ips)

print("✅ 提取完成：domains.yml & ips.yml 已生成！")
