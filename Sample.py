class ExpressionSolver:
    def __init__(self):
        # Operatör önceliklerini tanımlıyoruz
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.items = []

    def is_operator(self, char):
        return char in self.precedence

    def infix_to_postfix(self, expression):
        """
        Infix ifadeyi (A + B) Postfix ifadeye (A B +) dönüştürür.
        """
        stack = []  # Operatörler için yığıt
        output = []  # Sonuç listesi
        i = 0

        while i < len(expression):
            char = expression[i]

            # 1. Eğer karakter boşluksa atla
            if char == ' ':
                i += 1
                continue

            # 2. Eğer karakter sayı ise (çok basamaklı olabilir)
            if char.isdigit():
                num_str = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                output.append(num_str)  # Sayıyı çıktıya ekle
                continue  # Döngüde i zaten arttığı için continue kullanıyoruz

            # 3. Eğer karakter '(' ise yığıta ekle
            elif char == '(':
                stack.append(char)

            # 4. Eğer karakter ')' ise '(' görene kadar yığıttan çıkar
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # '(' karakterini de at

            # 5. Eğer karakter bir operatörse
            elif self.is_operator(char):
                while (stack and stack[-1] != '(' and
                       self.precedence.get(stack[-1], 0) >= self.precedence[char]):
                    # Yığıttaki operatörün önceliği mevcut operatörden büyük veya eşitse
                    # yığıttakini çıkar ve çıktıya ekle.
                    output.append(stack.pop())
                stack.append(char)

            i += 1

        # Yığıtta kalan tüm operatörleri boşalt
        while stack:
            output.append(stack.pop())

        return output

    def evaluate_postfix(self, postfix_list):
        """
        Postfix listesini hesaplar ve sonucu döndürür.
        """
        stack = []  # Sayılar (operandlar) için yığıt

        for token in postfix_list:
            # Eğer token sayı ise yığıta ekle
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))

            # Eğer token operatör ise işlem yap
            elif self.is_operator(token):
                if len(stack) < 2:
                    return "Hata: Yetersiz operand"

                val2 = stack.pop()  # LIFO: Önce çıkan ikinci sayıdır
                val1 = stack.pop()
                result = 0

                if token == '+':
                    result = val1 + val2
                elif token == '-':
                    result = val1 - val2
                elif token == '*':
                    result = val1 * val2
                elif token == '/':
                    result = val1 / val2
                elif token == '^':
                    result = val1 ** val2  # Üs alma

                stack.append(result)

        return stack[0]


# --- Test Kısmı ---
solver = ExpressionSolver()

input_expr = "3 + 4 * 2 / ( 1 - 5 ) ^ 2"
print(f"Girdi (Infix): {input_expr}")

# Adım 1: Dönüştürme
postfix_result = solver.infix_to_postfix(input_expr)
print(f"Postfix Hali: {' '.join(postfix_result)}")

# Adım 2: Hesaplama
final_result = solver.evaluate_postfix(postfix_result)
print(f"Sonuç: {final_result}")