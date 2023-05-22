from sklearn.metrics import f1_score, accuracy_score

# Read the predicted values from preds.txt
with open('pred.txt', 'r') as file:
    preds = file.readlines()

# Read the true values from true.txt
with open('true.txt', 'r') as file:
    true = file.readlines()

preds = [int(x) for x in preds[0].split()]


# Remove any trailing whitespaces or newlines from the lines
true = [int(x) for x in true[0].split()]

# Calculate weighted F1 score
f1_weighted = f1_score(true, preds, average='weighted')

# Calculate accuracy
accuracy = accuracy_score(true, preds)

# Print the results
print("Weighted F1 Score:", f1_weighted)
print("Accuracy:", accuracy)
