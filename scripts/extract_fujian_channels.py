import requests

# 原始直播源 URL
url = "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/live.txt"
response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    
    # 标记开始与结束的关键词
    start_marker = "☘️福建频道,#genre#"
    end_marker = "☘️甘肃频道,#genre#"

    # 提取福建频道段落
    collecting = False
    extracted_lines = []

    for line in lines:
        if start_marker in line:
            collecting = True
            extracted_lines.append("福建频道,#genre#")  # 替换标题行
            continue
        if collecting:
            if end_marker in line:
                break
            extracted_lines.append(line)

    # 写入目标文件
    with open("fujian_iptv.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(extracted_lines))

    print("✅ 福建频道已成功提取并保存为 fujian_iptv.txt")
else:
    print("❌ 获取 live.txt 文件失败。")
