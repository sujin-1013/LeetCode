class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        sec = 0

        new_tickets = [(idx, tickets[idx]) for idx in range(len(tickets))]
        
        while new_tickets:
            sec += 1

            idx, ticket = new_tickets.pop(0)

            if (ticket-1) != 0:
                new_tickets.append((idx, ticket-1))
            else:
                if idx == k:
                    return sec
            
        return sec
        