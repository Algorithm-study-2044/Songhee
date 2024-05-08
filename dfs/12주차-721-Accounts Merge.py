class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Helper function to find the root parent for any index.
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
      
        # The number of accounts.
        num_accounts = len(accounts)
      
        # Initialize a list where the value at index i is the parent of i.
        parent = list(range(num_accounts))
      
        # Dictionary to map each email to its account index.
        email_to_account_id = {}
      
        # Assign parents for accounts with shared emails.
        for account_id, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_id:
                    # Union operation: set the parent of the current account to the account 
                    # already associated with this email.
                    parent[find(account_id)] = find(email_to_account_id[email])
                else:
                    email_to_account_id[email] = account_id
      
        # Map each account index to a set of emails under the corresponding parent.
        emails_under_parent_account = defaultdict(set)
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                emails_under_parent_account[find(account_index)].add(email)
      
        # Compile the merged accounts: one per parent index.
        merged_accounts = []
        for parent_index, emails in emails_under_parent_account.items():
            # Sort the emails.
            sorted_emails = sorted(emails)
            # Prepend the account name.
            account_name = [accounts[parent_index][0]]
            merged_account = account_name + sorted_emails
            # Append the merged account to the result.
            merged_accounts.append(merged_account)
      
        return merged_accounts

# Note: List should be imported from typing to use it as a type hint in the function signature.
# from typing import List
