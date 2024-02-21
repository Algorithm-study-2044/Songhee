class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        res = []
        prev = products
        for i in range(len(searchWord)):
            tmp = []
            for product in prev:
                if len(product) > i and product[i] == searchWord[i]:
                    tmp.append(product)

            prev = tmp
            res.append(tmp[:3])

        return res