
6. <br/>
Скриншот с временем исполнения файла `filter.py`.<br/>  <br/>
![image](https://user-images.githubusercontent.com/53999702/142715453-ef39e22a-2a0b-499e-9719-9d5fea28c378.png)<br/> <br/>
Скриншот с временем исполнения файла `old-filter.py`.<br/> <br/>
![image](https://user-images.githubusercontent.com/53999702/142715128-06066be7-f465-4181-9ff0-06d7caed0790.png)

Изначально файл `filter.py` работает дольше, так как приходится вручную вводить данные из консоли. Чтобы замерить время без ввода в консоль запустим файл `filter_with_filename.py` с уже введенными данными.<br/>

![image](https://user-images.githubusercontent.com/53999702/142715485-3b74dba8-4893-42b7-ac73-c072dce6a2b5.png)

Различие во времени объясняется тем, что в Python циклы while работают медленнее чем for. Так же, итоговый код работает быстрее за счет использование библиотеки numpy. 
