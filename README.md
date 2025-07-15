Чтобы запустить все тесты нужно выполнить команду:

PYTHONPATH=. pytest tests/*

Восстановление пароля (recover_page.py)
test_recover_link - Переход на страницу восстановления пароля
test_request_password_recover - Ввод почты и клик по кнопке «Восстановить»
test_show_password - Показать/скрыть пароль

Личный кабинет (account_page.py)
test_account_link - Переход в личный кабинет
test_order_history - Переход в историю заказов
test_logout - Выход из системы

Проверка основного функционала (main_page.py)
test_constructor_link - Переход по клику на 'Конструктор'
test_orders_feed - Переход в ленту заказов
test_ingredient_modal - Открыть всплывающее окно ингредиентов
test_close_modal - Закрыть всплывающее окно
test_ingredients_counter - Проверка сетчика ингредиентов
test_create_order - Проверка создания заказа

Раздел "Лента заказов" (feed_page.py)
test_open_order - Проверка открытия заказа
test_users_order_in_order_feed - Заказы пользователя отображаются в ленте заказов
test_total_counter - Проверка увелечения счетчика за всё время
test_daily_counter - Проверка увелечения счетчика за сегодня
test_order_in_progress - Проверка номера оформленного заказа в разделе В работе