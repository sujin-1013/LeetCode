class Solution:
    def maskPII(self, s: str) -> str:
        
        # email
        if "@" in s:
            email_id = s.split("@")[0].lower()
            masking_email_id = email_id[0] + ("*" * 5) + email_id[-1]

            return masking_email_id + "@" + s.split("@")[1].lower()
        
        # phonenumber
        else:
            phone_number = ""
            for i in range(len(s)):
                if s[i] not in "-+() ":
                    phone_number += s[i]
                else:
                    continue

            print(phone_number)
            n = len(phone_number)
            last_pn = phone_number[n-4:n+1]
            
            if n == 11:
                masking_phone_number = "+*-***-***-" + last_pn
            elif n == 12:
                masking_phone_number = "+**-***-***-" + last_pn
            elif n == 13:
                masking_phone_number = "+***-***-***-" + last_pn
            else:
                masking_phone_number = "***-***-" + last_pn

            return masking_phone_number