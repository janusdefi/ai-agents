import numpy as np

class CertificateOfDeposit:
   def __init__(self, profit, liquidity_required, risk):
       self.profit = profit
       self.liquidity_required = liquidity_required
       self.risk = risk

def branch_and_bound(cds, max_liquidity, max_risk):
   # Sorting certificates based on profit-to-liquidity ratio (greedy heuristic)
   cds.sort(key=lambda cd: cd.profit / cd.liquidity_required, reverse=True)
   
   # Initialize variables for the best solution
   best_profit = 0
   best_combination = []
   
   # Stack for holding the branches in DFS order
   stack = [(0, 0, 0, [])]  # (current profit, current liquidity, current risk, included CDs)
   
   while stack:
       current_profit, current_liquidity, current_risk, included_cds = stack.pop()
       
       # Check if we've exceeded constraints
       if current_liquidity > max_liquidity or current_risk > max_risk:
           continue
       
       # Check if the current solution is better than the best found so far
       if current_profit > best_profit:
           best_profit = current_profit
           best_combination = included_cds
           
       # Explore further branches
       next_index = len(included_cds)
       if next_index < len(cds):
           cd = cds[next_index]
           
           # Branch 1: Include the next CD
           stack.append((
               current_profit + cd.profit,
               current_liquidity + cd.liquidity_required,
               current_risk + cd.risk,
               included_cds + [cd]
           ))
           
           # Branch 2: Do not include the next CD
           stack.append((current_profit, current_liquidity, current_risk, included_cds))
           
   return best_profit, best_combination

# Example usage:

# List of available certificates of deposit (profit, liquidity required, risk)
cds = [
   CertificateOfDeposit(profit=100, liquidity_required=50, risk=0.1),
   CertificateOfDeposit(profit=200, liquidity_required=60, risk=0.2),
   CertificateOfDeposit(profit=150, liquidity_required=70, risk=0.15),
   CertificateOfDeposit(profit=120, liquidity_required=40, risk=0.05)
]

max_liquidity = 150
max_risk = 0.3

best_profit, best_combination = branch_and_bound(cds, max_liquidity, max_risk)

print(f"Best Profit: {best_profit}")
print("Best Combination:")
for cd in best_combination:
   print(f"Profit: {cd.profit}, Liquidity Required: {cd.liquidity_required}, Risk: {cd.risk}")
