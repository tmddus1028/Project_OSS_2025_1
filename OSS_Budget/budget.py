import datetime
from expense import Expense
from collections import defaultdict

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def compare_monthly_spending(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return

        # 월별로 지출 그룹화
        monthly_totals = defaultdict(int)
        for e in self.expenses:
            # e.date는 'YYYY-MM-DD' 형식 → 'YYYY-MM'으로 자르기
            month_key = e.date[:7]
            monthly_totals[month_key] += e.amount

        # 출력 (월 순 정렬)
        print("\n[월별 지출 비교]")
        for month in sorted(monthly_totals):
            print(f"{month}: {monthly_totals[month]}원")
        print()
