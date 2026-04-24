import unittest
import sys
import io
from contextlib import redirect_stdout
import subprocess


class TestAppOutput(unittest.TestCase):
    """Тест для проверки вывода app.py"""
    
    def test_app_output(self):
        """Проверяет, что app.py выводит 'Hello, World!'"""
        # Захватываем stdout
        f = io.StringIO()
        with redirect_stdout(f):
            # Выполняем код из app.py, устанавливая __name__ = '__main__'
            with open('app.py', 'r') as file:
                code = file.read()
            # Создаем локальное пространство имен с __name__ = '__main__'
            namespace = {'__name__': '__main__', '__file__': 'app.py'}
            exec(code, namespace)
        
        output = f.getvalue()
        self.assertEqual(output.strip(), "Hello, World!")
    
    def test_app_output_via_subprocess(self):
        """Проверяет вывод через запуск app.py как скрипта"""
        result = subprocess.run(
            [sys.executable, 'app.py'],
            capture_output=True,
            text=True,
            cwd='.'
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, World!")


if __name__ == '__main__':
    unittest.main()

