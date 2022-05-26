class MoreThanFourDigits(Exception):
    """Raised when an input does not have 4 digits."""
    pass
class TooSimilar(Exception):
    """Raised when a four-digit number consists of the same digit."""

def kaprekar_count(n):
    """Finds the amount of 'Kaprekar's routines' it takes for a four-digit number to reach Kaprekar's constant: 6174."""

    def similarity_detector(n):
        """Detects if a number consists of the same four digits."""
        if n // 10 == 0:
            return True
        elif n % 10 != (n // 10) % 10:
            return False
        else:
            return similarity_detector(n // 10)
        
    try:
        if len(str(n)) > 4:
            raise MoreThanFourDigits
    except MoreThanFourDigits:
        print(f"Error: Argument must have at most 4 digits! \nShaving a digit off of the end. Your new number is now {n // 10}.")
        return kaprekar_count(n //  10)

    if len(str(n)) < 4:
        descending_list = sorted([i for i in str(n)], reverse = True)
        large_n = int("".join(descending_list))
        while len(str(large_n)) < 4:
            large_n *= 10
        ascending_list = sorted([i for i in str(n)])
        small_n =  int("".join(ascending_list))


    else:

        try: 
            if similarity_detector(n):
                raise TooSimilar
        except TooSimilar:
            return "Error: At least one digit must be unlike the others!"

        descending_list, ascending_list = sorted([i for i in str(n)], reverse = True), sorted([i for i in str(n)])
        large_n, small_n = int("".join(descending_list)), int("".join(ascending_list))
    
    difference = large_n - small_n 

    if difference == 6174:
        return 2
    else:
        return 1 + kaprekar_count(difference)