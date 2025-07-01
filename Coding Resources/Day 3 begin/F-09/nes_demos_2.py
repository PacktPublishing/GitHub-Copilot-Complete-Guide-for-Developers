def process_scores(scores):
  """Calculates the sum and average of a list of scores."""
  sum_count = 0 # We will rename this variable
  count = 0
  for score in scores:
    if isinstance(score, (int, float)) and score >= 0:
      sum_count = sum_count + score # Used here
      count += 1

  if count == 0:
    print("No valid scores provided.")
    return 0, 0.0

  average = sum_count / count # Used here
  print(f"Sum of scores: {sum_count}") # Used here
  print(f"Average score: {average}")
  return sum_count, average # Used here

# --- Usage Example ---
print("\nProcessing Scores:")
process_scores([10, 20, 30, -5, 15, "abc"])