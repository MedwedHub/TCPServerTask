TCP сервер, который распознаёт заданный формат данных, отображает его в требуемом формате и записывает во внешний файл. 

Формат данных BBBBxNNxHH:MM:SS.zhqxGGCR 
где BBBB - номер участника, x - пробельный символ, NN - id канала, HH - Часы MM - минуты, SS - секунды, zhq - десятые/сотые/тысячные, GG - номер группы CR - «возврат каретки» (закрывающий символ).

Пример данных: 0002 C1 01:13:02.877 00[CR]
Вывод: «спортсмен, нагрудный номер BBBB, прошёл отсечку NN в «время»" до десятых, сотые и тысячные отсекаются. Вывод только для группы 00; для остальных групп данные не отображаются, но пишутся в лог полностью.