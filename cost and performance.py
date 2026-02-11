input_tokens=int(input("enter input tokens:"))
output_tokens=int(input("enter output tokens:"))
cost_per_1000_tokens=0.002
total_tokens=input_tokens+output_tokens
total_cost=(total_tokens/1000)*cost_per_1000_tokens
print("\n total tokens:",total_tokens)
print("estimated cost($):",round(total_cost,6))