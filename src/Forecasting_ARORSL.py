# import numpy as np
# import matplotlib.pyplot as plt

# # -----------------------------
# # 1. AR(p) Online với RLS
# # -----------------------------
# class RLS_AR:
#     def __init__(self, p=5, lam=0.99, delta=1.0):
#         """
#         p: số bước lùi AR(p)
#         lam: forgetting factor (0<lam<=1)
#         delta: initial value cho ma trận P
#         """
#         self.p = p
#         self.lam = lam
#         self.theta = np.zeros((p,1))          # hệ số AR
#         self.P = np.eye(p) * delta            # ma trận P trong RLS
#         self.buffer = []

#     def update(self, x_new):
#         """
#         x_new: giá mới
#         """
#         if len(self.buffer) < self.p:
#             self.buffer.append(x_new)
#             return x_new  # chưa đủ dữ liệu
#         # chuẩn bị vector input
#         phi = np.array(self.buffer[-self.p:][::-1]).reshape(-1,1)  # x_t-1,...,x_t-p
#         y = np.array([[x_new]])
#         # gain
#         K = self.P @ phi / (self.lam + phi.T @ self.P @ phi)
#         # update theta
#         self.theta = self.theta + K @ (y - phi.T @ self.theta)
#         # update P
#         self.P = (self.P - K @ phi.T @ self.P) / self.lam
#         # cập nhật buffer
#         self.buffer.append(x_new)
#         return phi.T @ self.theta  # giá dự báo 1 bước

#     def forecast(self, h=5):
#         """
#         Dự báo h bước tới bằng recursive prediction
#         """
#         buf = self.buffer[-self.p:].copy()
#         preds = []
#         for _ in range(h):
#             phi = np.array(buf[-self.p:][::-1]).reshape(-1,1)
#             y_pred = float(phi.T @ self.theta)
#             preds.append(y_pred)
#             buf.append(y_pred)
#         return preds

# def LN_Forecasting_ARORSL(PG_cursor, PG_conn, model_LN_Forecasting):
#         query_DCS_Items = '''
#             SELECT 
#                 "CM_A181_V19_COM_V19_IN_5_PV3__Value", "CM_A181FT0010_DACA_PV__Value",
#                 "CM_A181FT0001_DACA_PV__Value", "CM_A181PT0013_DACA_PV__Value",
#                 "CM_A181AT0001_DACA_PV__Value", "CM_A181PT0002_DACA_PV__Value",
#                 "CM_A181PT0003_DACA_PV__Value", "CM_A181PT0004_DACA_PV__Value",
#                 "CM_A181PDT0002_DACA_PV__Value", "CM_A181PT0005_DACA_PV__Value",
#                 "CM_A181PT0006_DACA_PV__Value", "CM_A181PT0007_DACA_PV__Value",
#                 "CM_A181PT0008_DACA_PV__Value", "CM_A181TE0007_DACA_PV__Value",
#                 "CM_A181S015BPGPV_DACA_PV__Value", "CM_A181_TIEUHAOCO_OUT__Value" 
#             FROM "DCS_Items" 
#             ORDER BY "CronTime" DESC 
#             LIMIT 1'''
#         PG_cursor.execute(query_DCS_Items)
#         DCS_Items = PG_cursor.fetchone()
#         DCS_Items = [float(value) for value in DCS_Items]
#         print(DCS_Items)

#         ar_CM_A181_V19_COM_V19_IN_5_PV3__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181FT0010_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181FT0001_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0013_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181AT0001_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0002_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0003_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0004_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PDT0002_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0005_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0006_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0007_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181PT0008_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181TE0007_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181S015BPGPV_DACA_PV__Value = RLS_AR(p=60, lam=0.98, delta=0.5)
#         ar_CM_A181_TIEUHAOCO_OUT__Value = RLS_AR(p=60, lam=0.98, delta=0.5)

#         # Cập nhật giá mới mỗi cron
#         ar_CM_A181_V19_COM_V19_IN_5_PV3__Value.update(DCS_Items[0])
#         ar_CM_A181FT0010_DACA_PV__Value.update(DCS_Items[1])
#         ar_CM_A181FT0001_DACA_PV__Value.update(DCS_Items[2])
#         ar_CM_A181PT0013_DACA_PV__Value.update(DCS_Items[3])
#         ar_CM_A181AT0001_DACA_PV__Value.update(DCS_Items[4])
#         ar_CM_A181PT0002_DACA_PV__Value.update(DCS_Items[5])
#         ar_CM_A181PT0003_DACA_PV__Value.update(DCS_Items[6])
#         ar_CM_A181PT0004_DACA_PV__Value.update(DCS_Items[7])
#         ar_CM_A181PDT0002_DACA_PV__Value.update(DCS_Items[8])
#         ar_CM_A181PT0005_DACA_PV__Value.update(DCS_Items[9])
#         ar_CM_A181PT0006_DACA_PV__Value.update(DCS_Items[10])
#         ar_CM_A181PT0007_DACA_PV__Value.update(DCS_Items[11])
#         ar_CM_A181PT0008_DACA_PV__Value.update(DCS_Items[12])
#         ar_CM_A181TE0007_DACA_PV__Value.update(DCS_Items[13])
#         ar_CM_A181S015BPGPV_DACA_PV__Value.update(DCS_Items[14])
#         ar_CM_A181_TIEUHAOCO_OUT__Value.update(DCS_Items[15])

#         # Lấy giá dự báo 5 phút tới
#         pred_CM_A181_V19_COM_V19_IN_5_PV3__Value= ar_CM_A181_V19_COM_V19_IN_5_PV3__Value.forecast(5)
#         pred_CM_A181FT0010_DACA_PV__Value= ar_CM_A181FT0010_DACA_PV__Value.forecast(5)
#         pred_CM_A181FT0001_DACA_PV__Value= ar_CM_A181FT0001_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0013_DACA_PV__Value= ar_CM_A181PT0013_DACA_PV__Value.forecast(5)
#         pred_CM_A181AT0001_DACA_PV__Value= ar_CM_A181AT0001_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0002_DACA_PV__Value= ar_CM_A181PT0002_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0003_DACA_PV__Value= ar_CM_A181PT0003_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0004_DACA_PV__Value= ar_CM_A181PT0004_DACA_PV__Value.forecast(5)
#         pred_CM_A181PDT0002_DACA_PV__Value= ar_CM_A181PDT0002_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0005_DACA_PV__Value= ar_CM_A181PT0005_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0006_DACA_PV__Value= ar_CM_A181PT0006_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0007_DACA_PV__Value= ar_CM_A181PT0007_DACA_PV__Value.forecast(5)
#         pred_CM_A181PT0008_DACA_PV__Value= ar_CM_A181PT0008_DACA_PV__Value.forecast(5)
#         pred_CM_A181TE0007_DACA_PV__Value= ar_CM_A181TE0007_DACA_PV__Value.forecast(5)
#         pred_CM_A181S015BPGPV_DACA_PV__Value= ar_CM_A181S015BPGPV_DACA_PV__Value.forecast(5)
#         pred_CM_A181_TIEUHAOCO_OUT__Value= ar_CM_A181_TIEUHAOCO_OUT__Value.forecast(5)

#         print("pred_CM_A181_V19_COM_V19_IN_5_PV3__Value:", pred_CM_A181_V19_COM_V19_IN_5_PV3__Value)
#         print("pred_CM_A181FT0010_DACA_PV__Value:", pred_CM_A181FT0010_DACA_PV__Value)
#         print("pred_CM_A181FT0001_DACA_PV__Value:", pred_CM_A181FT0001_DACA_PV__Value)
#         print("pred_CM_A181PT0013_DACA_PV__Value:", pred_CM_A181PT0013_DACA_PV__Value)
#         print("pred_CM_A181AT0001_DACA_PV__Value:", pred_CM_A181AT0001_DACA_PV__Value)
#         print("pred_CM_A181PT0002_DACA_PV__Value:", pred_CM_A181PT0002_DACA_PV__Value)
#         print("pred_CM_A181PT0003_DACA_PV__Value:", pred_CM_A181PT0003_DACA_PV__Value)
#         print("pred_CM_A181PT0004_DACA_PV__Value:", pred_CM_A181PT0004_DACA_PV__Value)
#         print("pred_CM_A181PDT0002_DACA_PV__Value:", pred_CM_A181PDT0002_DACA_PV__Value)
#         print("pred_CM_A181PT0005_DACA_PV__Value:", pred_CM_A181PT0005_DACA_PV__Value)
#         print("pred_CM_A181PT0006_DACA_PV__Value:", pred_CM_A181PT0006_DACA_PV__Value)
#         print("pred_CM_A181PT0007_DACA_PV__Value:", pred_CM_A181PT0007_DACA_PV__Value)
#         print("pred_CM_A181PT0008_DACA_PV__Value:", pred_CM_A181PT0008_DACA_PV__Value)
#         print("pred_CM_A181TE0007_DACA_PV__Value:", pred_CM_A181TE0007_DACA_PV__Value)
#         print("pred_CM_A181S015BPGPV_DACA_PV__Value:", pred_CM_A181S015BPGPV_DACA_PV__Value)
#         print("pred_CM_A181_TIEUHAOCO_OUT__Value:", pred_CM_A181_TIEUHAOCO_OUT__Value)
        
import numpy as np
from datetime import datetime, timedelta
import pickle
import os

class RLS_AR:
    def __init__(self, p=5, lam=0.98, delta=0.5):
        self.p = p
        self.lam = lam
        self.theta = np.zeros((p,1))
        self.P = np.eye(p) * delta
        self.buffer = []

    def update(self, x_new):
        if len(self.buffer) < self.p:
            self.buffer.append(x_new)
            return None
        phi = np.array(self.buffer[-self.p:][::-1]).reshape(-1,1)
        y = np.array([[x_new]])
        K = self.P @ phi / (self.lam + phi.T @ self.P @ phi)
        self.theta = self.theta + K @ (y - phi.T @ self.theta)
        self.P = (self.P - K @ phi.T @ self.P) / self.lam
        self.buffer.append(x_new)
        if len(self.buffer) > 1000:
            self.buffer = self.buffer[-1000:]
        return float(phi.T @ self.theta)

    # def forecast(self, h=5):
    #     buf = self.buffer[-self.p:].copy()
    #     preds = []
    #     for _ in range(h):
    #         phi = np.array(buf[-self.p:][::-1]).reshape(-1,1)
    #         y_pred = float(phi.T @ self.theta)
    #         preds.append(y_pred)
    #         buf.append(y_pred)
    #     return preds
    def forecast(self, h=5):
        """
        Dự báo h bước tới bằng recursive prediction
        """
        if len(self.buffer) < self.p:
            # chưa đủ dữ liệu để dự báo
            return [np.nan] * h

        buf = self.buffer[-self.p:].copy()
        preds = []
        for _ in range(h):
            phi = np.array(buf[-self.p:][::-1]).reshape(-1, 1)
            y_pred = float(phi.T @ self.theta)
            preds.append(y_pred)
            buf.append(y_pred)
        return preds

# -----------------------------
# HÀM CHÍNH CHẠY MỖI CRON
# -----------------------------
def LN_Forecasting_ARORSL(PG_cursor, PG_conn, model_dir="../models_rls"):
    os.makedirs(model_dir, exist_ok=True)

    # Danh sách cột DCS
    columns = [
        "CM_A181_V19_COM_V19_IN_5_PV3__Value", "CM_A181FT0010_DACA_PV__Value",
        "CM_A181FT0001_DACA_PV__Value", "CM_A181PT0013_DACA_PV__Value",
        "CM_A181AT0001_DACA_PV__Value", "CM_A181PT0002_DACA_PV__Value",
        "CM_A181PT0003_DACA_PV__Value", "CM_A181PT0004_DACA_PV__Value",
        "CM_A181PDT0002_DACA_PV__Value", "CM_A181PT0005_DACA_PV__Value",
        "CM_A181PT0006_DACA_PV__Value", "CM_A181PT0007_DACA_PV__Value",
        "CM_A181PT0008_DACA_PV__Value", "CM_A181TE0007_DACA_PV__Value",
        "CM_A181S015BPGPV_DACA_PV__Value", "CM_A181_TIEUHAOCO_OUT__Value",
        "CM_A181TE0023_DACA_PV__Value", "CM_A181AT0004_DACA_PV__Value",
        "CM_A181LT0001_DACA_PV__Value"
    ]

    col_str = ",".join([f'"{c}"' for c in columns])
    query = f'SELECT {col_str} FROM "DCS_Items" ORDER BY "CronTime" DESC LIMIT 1'   
    PG_cursor.execute(query)
    DCS_Items = [float(v) for v in PG_cursor.fetchone()]

    preds_5 = {}

    for i, col in enumerate(columns):
        model_path = os.path.join(model_dir, f"{col}.pkl")

        # Load mô hình nếu có, nếu không thì khởi tạo mới
        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                ar_model = pickle.load(f)
        else:
            ar_model = RLS_AR(p=30, lam=0.98, delta=0.5)

        # Cập nhật giá trị mới
        ar_model.update(DCS_Items[i])

        # Lưu lại mô hình (để dùng cho lần cron sau)
        with open(model_path, "wb") as f:
            pickle.dump(ar_model, f)

        # Dự báo 5 phút
        preds_5[col] = ar_model.forecast(5)

    # In thử kết quả
    for k, v in preds_5.items():
        print(f"{k}: {v[:5]}")

    # Lưu vào DB
    # PG_cursor.execute('SELECT * FROM "DATA_LN_Forecasting" LIMIT 1')
    name_columns = ["CronTime"] + columns
    placeholders = ', '.join(['%s'] * len(name_columns))
    columns_db = ', '.join([f'"{col}"' for col in name_columns])

    # Lấy thời gian hiện tại làm mốc
    crontime = datetime.now().replace(second=0, microsecond=0)

    for i in range(5):
        LN_Forecasting = [preds_5[col][i] for col in columns]
        values = [crontime + timedelta(minutes=i+1)] + [float(x) for x in LN_Forecasting]
        print("values:", values)

        insert_query = f'INSERT INTO "DATA_LN_Forecasting" ({columns_db}) VALUES ({placeholders})'
        try:
            PG_cursor.execute(insert_query, values)
            PG_conn.commit()
        except Exception as e:
            PG_conn.rollback()
            print(f"[DB ERROR] {e}")

    print("[✅] Inserted 5-step forecast into DB successfully.")