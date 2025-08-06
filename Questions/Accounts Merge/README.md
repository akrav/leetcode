[Back to Table of Contents](../../README.md)

# Accounts Merge
Difficulty: Medium

## Question
Accounts Merge
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

## Solution Template
```python
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         accounts_map = defaultdict(list)
#         account_to_name = defaultdict(str)

#         for i in range(len(accounts)):
#             account_to_name[i] = accounts[i][0]
#             accounts_map[accounts[i][1]] = []
#             for j in range(2, len(accounts[i])):
#                 accounts_map[accounts[i][1]].append(accounts[i][j])
        
#         print(f"account_to_name: {account_to_name}")
#         print(f"accounts_map: {accounts_map}")
                
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         uf = UnionFind()
#         email_to_name = {}
        
#         # Step 1: Initialize the UnionFind structure and map each email to a name.
#         for account in accounts:
#             name = account[0]
#             first_email = account[1]
#             uf.add(first_email)
#             email_to_name[first_email] = name
#             # Union all emails in the current account.
#             for email in account[1:]:
#                 uf.add(email)
#                 email_to_name[email] = name
#                 uf.union(first_email, email)
#                 print(f"uf.parent: {uf.parent}")
        
#         # Step 2: Group emails by their root parent.
#         components = {}
#         for email in email_to_name:
#             root = uf.find(email)
#             print(f"email: {email}, root: {root}")
#             if root not in components:
#                 components[root] = []
#             components[root].append(email)
        
#         print(f"\ncomponents: {components}\n")
        
#         # Step 3: Build the final merged accounts list.
#         merged_accounts = []
#         for root, emails in components.items():
#             merged_accounts.append([email_to_name[root]] + sorted(emails))
        
#         return merged_accounts

# # UnionFind class as defined above.
# class UnionFind:
#     def __init__(self):
#         self.parent = {}
    
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union(self, x, y):
#         rootX = self.find(x)
#         rootY = self.find(y)
#         if rootX != rootY:
#             self.parent[rootY] = rootX
    
#     def add(self, x):
#         if x not in self.parent:
#             self.parent[x] = x


class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
    
    def find(self, x):
        if self.parent[x] != x:
             self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            self.parent[parentY] = parentX

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            uf.add(first_email)
            for email in account[1:]:
                uf.add(email)
                email_to_name[email] = name
                uf.union(first_email, email)
        

        comparison = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            comparison[root].append(email)
        

        ans = []
        for key, val in comparison.items():
            ans.append([email_to_name[key]]+sorted(val))
        
        return ans
```
