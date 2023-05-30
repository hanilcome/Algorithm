def solution(numbers):
        num = 0
        number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        for a in number:        
                numbers = numbers.replace(a, str(num))
                num += 1
                
        return int(numbers)