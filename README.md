# co-purchase-network

Network Analysis for Identifying Product Relationships and Cross-selling Opportunities Using the UCI Online Retail Dataset.

Project nghiên cứu cá nhân sử dụng Python, pandas, NetworkX, Matplotlib và Seaborn. Mục tiêu là khảo sát cấu trúc mua chung, vai trò của sản phẩm trong mạng và các association rules phục vụ đánh giá cơ hội cross-selling.

## Research questions

- **RQ1:** Mạng mua chung thể hiện những cộng đồng sản phẩm nào, và cấu trúc đó ổn định đến mức nào khi thay đổi tham số, random seed hoặc loại các hóa đơn lớn?
- **RQ2:** Những sản phẩm nào nổi bật theo degree, weighted degree (strength) và betweenness centrality?
- **RQ3:** Những cặp sản phẩm nào có association rules đáng xem xét, dựa trên support, confidence, lift, mức độ phụ thuộc hóa đơn lớn và đánh giá nghiệp vụ?

## Dataset và cấu trúc

Nguồn: [UCI Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail), Daqing Chen (2015), [DOI: 10.24432/C5BW33](https://doi.org/10.24432/C5BW33). Tải và giải nén thủ công, đặt file đúng tên `data/raw/Online Retail.xlsx`. Các notebook không tự tải dữ liệu.

SHA256 của file Excel dùng trong lần review này:

```text
43465a06f2ccf7c8b5bd2892bc7defb52f97487934fe93b16ae4c3936424676d
```

```text
config.py                     # Đường dẫn tương đối với project và tham số dùng chung
AGENTS.md                     # Ownership và giới hạn sửa file
requirements.txt              # Dependencies chính với phiên bản cố định
data/raw/                     # Excel gốc, không quản lý bằng Git
data/processed/               # Parquet và CSV Phase 1, không quản lý bằng Git
notebooks/
  01_eda.ipynb
  02_network_construction.ipynb
  03_network_analysis.ipynb
  04_cross_selling.ipynb
  05_visualization.ipynb
outputs/networks/             # GraphML và network_summary.json
outputs/tables/               # Bảng kết quả và Business Review thủ công
outputs/figures/              # 7 figure PNG của Phase 5
```

## Tạo môi trường

Môi trường đã kiểm tra sử dụng **Python 3.12.4**. Thực hiện các lệnh dưới đây tại thư mục gốc project trên macOS/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name co-purchase-network --display-name "Python (co-purchase-network)"
python -m jupyterlab
```

`openpyxl` hỗ trợ đọc Excel, `pyarrow` hỗ trợ đọc/ghi Parquet và Pillow được notebook 05 dùng để kiểm tra PNG. Các phiên bản trong `requirements.txt` được lấy từ môi trường hiện tại, chưa được kiểm chứng bằng một lần cài mới từ đầu và chưa phải lockfile đầy đủ cho các dependency gián tiếp.

## Thứ tự chạy

Mở notebook từ thư mục gốc hoặc `notebooks/`, chọn kernel **Python (co-purchase-network)**, rồi dùng **Restart Kernel and Run All Cells** cho từng notebook. Lưu notebook sau khi chạy để giữ các bảng và diễn giải được hiển thị.

Thứ tự cho toàn bộ kết quả hiện tại:

**01 → 02 → 03 → 04 → kiểm tra Business Review → 05.**

Phase 04 có thể tính association rules mà thiếu Phase 03, nhưng lúc đó không tích hợp community và không áp dụng giới hạn số rule theo cặp community. Vì shortlist và notebook 05 sử dụng community metadata, cần chạy **03 trước 04** khi tái lập toàn bộ nghiên cứu.

| Notebook | Inputs chính | Outputs được lưu |
| --- | --- | --- |
| 01 | `data/raw/Online Retail.xlsx` | `data/processed/cleaned_transactions.parquet`, `invoice_items.parquet`, hai bản CSV cùng tên; `outputs/tables/data_quality.csv` |
| 02 | Hai file Parquet Phase 1, `config.py` | `outputs/tables/selected_products.csv`, `pair_counts.csv`; `outputs/networks/product_network.graphml`, `network_summary.json` |
| 03 | GraphML, JSON, selected products và pair counts của Phase 2; `invoice_items.parquet` cho large-invoice robustness | `outputs/tables/node_metrics.csv`, `community_summary.csv`, `community_stability.csv`, `candidate_network_comparison.csv` |
| 04 | `invoice_items.parquet`, selected products, pair counts và `network_summary.json`; `node_metrics.csv` để tích hợp community | `outputs/tables/cross_selling_candidates.csv`, `cross_selling_shortlist.csv` |
| 05 | Outputs Phase 2–4 và `outputs/tables/cross_selling_business_review.csv` | 7 PNG trong `outputs/figures/`; các bảng diễn giải hiển thị trong notebook |

Các file trong `data/raw/` và `data/processed/` được Git bỏ qua, vì vậy clone repository chưa cung cấp đầy đủ input để chạy ngay Phase 02–04. Chạy Phase 01 để tạo lại processed data. Giữ các thư mục `data/raw`, `data/processed`, `outputs/tables`, `outputs/networks`, `outputs/figures`; chúng được giữ bằng `.gitkeep` trong repository.

Chạy lại notebook sẽ cập nhật các output tương ứng. Phase 02 có cache pair counts gắn với checksum của input; không cần xóa output cũ để chạy lại. Sau thay đổi cleaning hoặc Excel, chạy lại từ 01. Sau thay đổi cấu hình mạng, chạy lại từ 02 và toàn bộ các bước phía sau. **Restart kernel sau khi sửa `config.py`**, vì Python có thể giữ module config đã import trong kernel.

Notebook 03 bỏ qua ứng viên vượt phạm vi selected products đã lưu. Notebook 05 hiện chỉ hỗ trợ cấu hình chính thức **Top 100 / threshold 125** và yêu cầu các bảng upstream khớp cấu hình đó; các thử nghiệm Top 50/75 không tự động tạo được bộ figure cuối cùng.

## Business Review trước Phase 05

`outputs/tables/cross_selling_business_review.csv` là **đầu vào đánh giá thủ công đã được quản lý bằng Git**. Không notebook nào tự tạo hoặc tự cập nhật file này. Không dùng toàn bộ candidate pool thay cho shortlist để review.

- Giữ nguyên file review khi chạy lại 04 cho ra cùng shortlist và các chỉ số không đổi.
- Nếu shortlist, chỉ số hoặc community thay đổi, cập nhật review theo đúng từng cặp có hướng `antecedent`, `consequent` của shortlist mới trước khi chạy 05.
- Copy chính xác các cột `pair_count`, `pair_support`, `confidence`, `lift`, `large_invoice_pair_share`, `antecedent_community`, `consequent_community`, `same_community` từ shortlist; không nhập lại số đã làm tròn.
- Đánh giá `relationship_type` với một trong các giá trị `same-product-family`, `potential-complementary`, `potential-substitute`, `unclear`; điền `business_relevance`, `review_reason` và `review_status = Reviewed`.
- Số dòng và khóa rule phải khớp hoàn toàn với shortlist. Dùng dấu chấm thập phân: `0.125` tương đương 12.5%. Notebook 05 hỗ trợ dấu phân cách comma, semicolon hoặc tab; file hiện tại dùng semicolon.

Notebook 05 kiểm tra các điều kiện trên và dừng nếu review thiếu hoặc không còn khớp, thay vì sử dụng nhãn cũ. Những nhận xét định tính theo community trong notebook 05 và bảng manual shortlist lịch sử trong notebook 04 cũng cần được xem lại khi dữ liệu hoặc phân hoạch thay đổi.

## Quy ước và kiểm tra kết quả

- Hóa đơn được xác định bằng `InvoiceNo`, sản phẩm bằng `StockCode`; `invoice_items` có đúng một dòng cho mỗi cặp hóa đơn–sản phẩm.
- Phase 01 giữ exact duplicate transaction rows theo phương pháp đã ghi trong notebook. Chúng không làm tăng pair counts vì các phép tính mua chung dùng `invoice_items` đã loại trùng cặp.
- `pair_counts.csv` chứa mọi cặp quan sát được trong phạm vi Top N trước khi lọc graph. Graph vô hướng dùng `weight = pair_count` và chỉ giữ cạnh đạt `MIN_EDGE_WEIGHT`, nhưng giữ tất cả selected nodes.
- Strength là tổng trọng số cạnh; betweenness dùng khoảng cách `1 / weight`. Louvain và modularity dùng trọng số; ARI so sánh assignments trên cùng tập sản phẩm, không so trực tiếp community IDs.
- Support dùng **toàn bộ hóa đơn hợp lệ đã cleaning** làm mẫu số. Confidence có hướng; lift và pair support đối xứng. `MIN_RULE_PAIR_COUNT` độc lập với threshold của graph.
- Hóa đơn lớn là hóa đơn có ít nhất 100 sản phẩm phân biệt, tính trên toàn bộ basket trước khi lọc Top N. Phase 03 tính lại pair counts cho sensitivity scenario vì Phase 02 chưa lưu bảng pair counts phù hợp cho scenario này; đây là phân tích robustness, không cleaning lại dữ liệu.
- Các bảng C3/C5 và kết quả large-invoice robustness của Phase 03 được hiển thị trong notebook, chưa xuất thành CSV riêng. Cần giữ notebook đã chạy khi trích evidence cho báo cáo.

Với file Excel có checksum trên và cấu hình hiện tại (`TOP_N_PRODUCTS=100`, `MIN_EDGE_WEIGHT=125`, `MIN_RULE_PAIR_COUNT=5`, `RANDOM_STATE=42`), lần review ghi nhận các mốc tham chiếu:

| Kết quả | Giá trị |
| --- | --- |
| Dòng raw | 541,909 |
| Dòng cleaned transactions | 527,746 |
| Cặp invoice–product phân biệt | 517,275 |
| Hóa đơn hợp lệ dùng làm mẫu số association | 19,773 |
| Graph chính thức | 100 nodes, 2,074 edges |
| Louvain, seed 42, resolution 1 | 5 communities; weighted modularity ≈ 0.184622 |
| Cross-selling candidates / shortlist | 9,794 directed rules / 20 rules |

Đây là kết quả tham chiếu cho snapshot dữ liệu và môi trường này, không phải điều kiện ép kết quả khi thay đổi tham số hay dữ liệu. Các ngưỡng trong config là tham số nghiên cứu, không chứng minh một network tối ưu. Association và community chưa đủ để khẳng định hiệu quả cross-selling thực tế.

## Nguồn dữ liệu cho 7 figure

Tất cả figure được notebook 05 dựng từ saved outputs, không đọc lại Excel hoặc chạy lại Louvain, centrality hay association rules. Hai hình network tính layout để hiển thị và chỉ vẽ các cạnh thuộc nhóm trọng số cao nhất theo P90; các chỉ số vẫn lấy từ graph đầy đủ.

| PNG trong `outputs/figures/` | Nguồn chính |
| --- | --- |
| `rq1_community_network.png` | `product_network.graphml` + `node_metrics.csv` + `community_summary.csv` |
| `rq1_community_sizes.png` | `community_summary.csv` |
| `rq2_top_strength.png` | `node_metrics.csv` |
| `rq2_top_betweenness.png` | `node_metrics.csv` |
| `rq2_central_products_network.png` | `product_network.graphml` + `node_metrics.csv` |
| `rq3_association_heatmap.png` | `cross_selling_candidates.csv` cho pair support; `cross_selling_shortlist.csv` và `node_metrics.csv` để chọn/nhóm sản phẩm |
| `rq3_support_vs_lift.png` | `cross_selling_candidates.csv` + `cross_selling_shortlist.csv` + `cross_selling_business_review.csv` |

PNG được lưu ở 300 DPI. Giữ graph, các bảng phân tích và Business Review đồng bộ trước khi tái tạo figure.

