from http.server import BaseHTTPRequestHandler, HTTPServer

# Настройки запуска веб-приложения
host_name = 'localhost'  # Адрес
server_port = 8080  # Порт


class MyServer(BaseHTTPRequestHandler):
    """
           Специальный класс, который отвечает за
           обработку входящих запросов от клиентов
       """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header('Content-type', 'application/json')  # Отправка типа данных
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes("Hello, World wide web!", "utf-8"))  # Тело ответа

    def do_POST(self):
        """Метод для обработки POST-запросов"""
        print(self.headers.items())  # Вывод в консоль информации о запросе
        content_length = int(self.headers.get('Content-Length'))  # Нахождение длины данных, переданных пользователем
        content_data = self.rfile.read(content_length)  # чтение данных, переданных пользователем
        print(content_data.decode())  # Вывод в консоль данных, переданных пользователем


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")