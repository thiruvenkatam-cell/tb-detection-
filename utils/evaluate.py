from utils.metrics import sensitivity, specificity

tp, tn, fp, fn = 90, 85, 10, 15

print("Sensitivity:", sensitivity(tp, fn))
print("Specificity:", specificity(tn, fp))
