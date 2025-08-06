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