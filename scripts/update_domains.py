import requests
import yaml
import re
import socket

# M3U 直播源列表（修改为你的源）
M3U_URLS = [
    "https://raw.githubusercontent.com/YueChan/Live/main/Global.m3u"
]

# 正则表达式：提取域名
DOMAIN_PATTERN = re.compile(r'https?://([^:/]+)')

def extract_domains_and_ips(m3u_urls):
    """从多个 M3U 文件提取域名和 IP 地址，并去重"""
    domains = set()
    ips = set()

    for url in m3u_urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # 提取域名
            domains.update(DOMAIN_PATTERN.findall(response.text))

            # 提取 IP 地址
            for domain in domains:
                try:
                    ip = socket.gethostbyname(domain)
                    ips.add(ip)
                except socket.gaierror:
                    continue
        except requests.RequestException as e:
            print(f"无法获取 {url}: {e}")

    return sorted(domains), sorted(ips)

def update_yaml(domains, ips):
    """更新 domains.yml 和 ips.yml 文件"""
    
    # 更新域名文件
    domain_data = {"payload": domains}
    with open("domains.yml", "w", encoding="utf-8") as domain_file:
        yaml.dump(domain_data, domain_file, allow_unicode=True, default_flow_style=False)

    # 更新 IP 文件
    ip_data = {"payload": ips}
    with open("ips.yml", "w", encoding="utf-8") as ip_file:
        yaml.dump(ip_data, ip_file, allow_unicode=True, default_flow_style=False)

def main():
    # 获取域名和 IP 地址
    domains, ips = extract_domains_and_ips(M3U_URLS)
    
    # 更新 YAML 文件
    update_yaml(domains, ips)

if __name__ == "__main__":
    main()
