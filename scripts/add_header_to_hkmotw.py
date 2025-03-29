import requests

# 下载文件内容
url = "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/%E4%B8%93%E5%8C%BA/%E2%99%AA%E6%B8%AF%E6%BE%B3%E5%8F%B0.txt"
response = requests.get(url)

if response.status_code == 200:
    # 获取文件内容
    content = response.text

    # 新增的行
    new_line = "港澳台频道,#genre#\n"

    # 将新行添加到文件内容的顶部
    updated_content = new_line + content

    # 将更新后的内容保存到文件
    with open("HKMOTW.txt", "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Header added successfully!")
else:
    print("Failed to download the file.")
