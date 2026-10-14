# 当前数据与统计复算 2026-10-13

本版对应最新学术论证稿：30题270条事后合规审计，12题36条首次有效人工审核，外部10题90条GLM匿名异源复评。三种评价分开，不合并分母。

运行 `python3 reproduce_current.py`（Python3.10以上，仅标准库）输出三个数据层的计数与GLM题目簇bootstrap区间。main30.csv为事后核查标签，不是独立评分；human12.csv的建议与方法可见，不能计算独立盲评可靠性。glm_external10.csv为完整异源机器结果，字段矛盾不用于计算无依据补充率。

external_answers90.json及main30.csv保存生成回答；evidence_locations.json保存原文页码定位与文本哈希，不分发第三方文献全文或长摘录。仅凭本包不能重新审查全部原文支持关系，需合法访问对应原文。模型快照及随机参数未固定，不能保证逐字端到端复现。config记录可确认的配置与缺口。

仓库早期research_data_and_code.zip和reproduce.py属于历史版本，不能用于复算当前稿。本版请使用current_data_20261013.zip；代码与衍生数据尚未另行授予开放许可证，公开访问不代表第三方原文授权。无DOI，仓库提交链接固定本版内容。
