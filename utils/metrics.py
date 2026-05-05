def sensitivity(tp, fn):
    return tp / (tp + fn + 1e-8)

def specificity(tn, fp):
    return tn / (tn + fp + 1e-8)
