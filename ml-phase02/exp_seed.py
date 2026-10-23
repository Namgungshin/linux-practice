import importlib
import numpy as np

m = importlib.import_module("01_ml_intro")

def run(data_seed, split_seed):
    X, y = m.generate_classification_data(n_per_class=150, separation=2.0, seed=data_seed)
    X_tr, X_te, y_tr, y_te = m.train_test_split(X, y, seed=split_seed)
    clf = m.NearestCentroid()
    clf.fit(X_tr, y_tr)
    return clf.score(X_tr, y_tr), clf.score(X_te, y_te)

def summarize(name, test_accs):
    a = np.array(test_accs)
    print(f"{name:<28} mean={a.mean():.3f}  std={a.std():.3f}  min={a.min():.3f}  max={a.max():.3f}")

# 실험 1: 데이터는 고정(42), 분할 시드만 변경
res1 = [run(42, s)[1] for s in range(30)]
summarize("split seed 0~29 (data fixed)", res1)

# 실험 2: 분할은 고정(42), 데이터 시드만 변경
res2 = [run(s, 42)[1] for s in range(30)]
summarize("data seed 0~29 (split fixed)", res2)

# 원래 레슨 결과 재현
tr, te = run(42, 42)
print(f"\nlesson default (42, 42): train={tr:.3f} test={te:.3f}")
