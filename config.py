"""Đường dẫn và cấu hình ban đầu; các ngưỡng cần được kiểm chứng khi nghiên cứu."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RAW_DATA_FILE = RAW_DATA_DIR / "Online Retail.xlsx"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
NETWORKS_DIR = OUTPUTS_DIR / "networks"
TABLES_DIR = OUTPUTS_DIR / "tables"
FIGURES_DIR = OUTPUTS_DIR / "figures"

REPORTS_DIR = PROJECT_ROOT / "reports"
PAPER_DIR = REPORTS_DIR / "paper"
SLIDES_DIR = REPORTS_DIR / "slides"

# Giá trị khởi đầu, chưa phải các lựa chọn đã được xác thực bằng dữ liệu.
TOP_N_PRODUCTS = 100
MIN_EDGE_WEIGHT = 3
MIN_RULE_PAIR_COUNT = 5
RANDOM_STATE = 42
