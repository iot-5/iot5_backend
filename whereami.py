from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import make_pipeline

import json
from collections import Counter
import os
import pickle

def aps_to_dict(aps):
    return {ap['ssid'] + " " + ap['bssid']: ap['quality'] for ap in aps}


def get_train_data(folder=None):
    if folder is None:
        folder = ensure_whereami_path()
    X = []
    y = []
    for fname in os.listdir(folder):
        if fname.endswith(".txt"):
            data = []
            with open(os.path.join(folder, fname)) as f:
                for line in f:
                    data.append(json.loads(line))
            X.extend(data)
            y.extend([fname.rstrip(".txt")] * len(data))
    return X, y



def write_data(label_path, data):
    with open(label_path, "a") as f:
        f.write(json.dumps(data))
        f.write("\n")


def learn(label, n=1, device="", data=None):
    path = ensure_whereami_path()
    label_path = get_label_file(path, label + ".txt")

    new_sample = data
    write_data(label_path, new_sample)

    train_model()


class LearnLocation(Exception):
    pass


def get_pipeline(clf=RandomForestClassifier(n_estimators=100, class_weight="balanced")):
    return make_pipeline(DictVectorizer(sparse=False), clf)


def train_model(path=None):
    model_file = get_model_file(path)
    X, y = get_train_data(path)
    if len(X) == 0:
        raise ValueError("No wifi access points have been found during training")
    # fantastic: because using "quality" rather than "rssi", we expect values 0-150
    # 0 essentially indicates no connection
    # 150 is something like best possible connection
    # Not observing a wifi will mean a value of 0, which is the perfect default.
    lp = get_pipeline()
    lp.fit(X, y)
    with open(model_file, "wb") as f:
        pickle.dump(lp, f)
    return lp


def get_model(path=None):
    model_file = get_model_file(path)
    if not os.path.isfile(model_file):  # pragma: no cover
        msg = "First learn a location, e.g. with `whereami learn -l kitchen`."
        return None
        raise LearnLocation(msg)
    with open(model_file, "rb") as f:
        lp = pickle.load(f)
    return lp


def crossval(clf=None, X=None, y=None, folds=10, n=5, path=None):
    if X is None or y is None:
        X, y = get_train_data(path)
    if len(X) < folds:
        raise ValueError('There are not enough samples ({}). Need at least {}.'.format(len(X), folds))
    clf = clf or get_model(path)
    tot = 0
    print("KFold folds={}, running {} times".format(folds, n))
    for i in range(n):
        res = cross_val_score(clf, X, y, cv=folds).mean()
        tot += res
        print("{}/{}: {}".format(i + 1, n, res))
    print("-------- total --------")
    print(tot / n)
    return tot / n


def locations(path=None):
    _, y = get_train_data(path)
    if len(y) == 0:  # pragma: no cover
        msg = "No location samples available. First learn a location, e.g. with `whereami learn -l kitchen`."
        print(msg)
    else:
        occurrences = Counter(y)
        for key, value in occurrences.items():
            print("{}: {}".format(key, value))


def get_whereami_path(path=None):
    if path is None:
        _USERNAME = os.getenv("SUDO_USER") or os.getenv("USER") or "/"
        path = os.path.expanduser('~' + _USERNAME)
        path = os.path.join(path, ".whereami")
    return os.path.expanduser(path)


def ensure_whereami_path():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, ".whereami")
    if not os.path.exists(path):  # pragma: no cover
        os.makedirs(path)
    return path


def get_model_file(path=None, model="model.pkl"):
    path = ensure_whereami_path() if path is None else path
    return os.path.join(path, model)


def get_label_file(path, label):
    return os.path.join(get_whereami_path(path), label)


def rename_label(label, new_label, path=None):
    path = ensure_whereami_path() if path is None else path
    from_path = os.path.join(path, label + ".txt")
    new_path = os.path.join(path, new_label + ".txt")
    os.rename(from_path, new_path)
    print("Renamed {} to {}".format(from_path, new_path))



class Predicter():
    def __init__(self, model=None):
        self.model = model
        self.clf = get_model(model)
        self.predicted_value = None

    def predict(self, aps):
        self.refresh()
        self.predicted_value = self.clf.predict(aps_to_dict(aps))[0]
        return self.predicted_value

    def refresh(self):
        self.clf = get_model(self.model)

