class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace("-", "")

        if s == "":
            return ""

        reversed_s = s[::-1]

        reformatted_key = ""

        while True:
            if len(reversed_s) < k:
                reformatted_key += reversed_s[:k]
                break

            reformatted_key += reversed_s[:k] + "-"
            reversed_s = reversed_s[k:]

        reformatted_key = reformatted_key[::-1].upper()

        if reformatted_key[0] == "-":
            return reformatted_key[1:]
        
        return reformatted_key