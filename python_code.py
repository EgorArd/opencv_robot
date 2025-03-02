import cv2 #библиотека компьютерного зрения
import serial #библиотека общения с arduino

cap = cv2.VideoCapture(0) #выбор захвата вебки
serial = serial.Serial('/dev/ttyACM0', 9600) #serial данные arduino (сом порт и скорость)

cap.set(3, 640) #ширина 
cap.set(4, 480) #высота
cap.set(cv2.CAP_PROP_FPS, 30) #частота кадров - для raspberry pi ОБЯЗАТЕЛЬНАЯ настройка

while True:
    ret, frame = cap.read() #чтение изображения с вебки
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #преобразование в черно-белое изображение

    blurred = cv2.GaussianBlur(gray, (5, 5), 0) #размытие изображения
    edges = cv2.Canny(blurred, 100, 150) #порог цветов - точность определения
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #нахождение контуров

    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea) #поиск контура с максимальной площадью
        x, y, w, h = cv2.boundingRect(max_contour) # кординаты для рисования прямоугольника на линии

        center_x = x + w // 2
        center_y = y + h // 2
        print(f"x: {center_x} \n y {center_y}") #вывод кординат центра линии

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) #рисование прямоуголльника
        cv2.circle(frame, (center_x, center_y), 7, (0, 0, 255), -1) #рисование круга

        if center_x >= 250 and center_x <= 350: #если нет отклонение от центра по x
            serial.write(b'f') #отправляем 'f'

        elif center_x > 350 and center_x <= 500: #если есть отклонение от центра по x вправо 
            serial.write(b'e') #отправляем 'e'
            
        elif center_x < 250 and center_x >= 100: #если есть отклонение от центра по x влево 
            serial.write(b'r') #отправляем 'r'
            
        else:
            serial.write(b'd') #в другом случае -> отправляем 'd'

    cv2.imshow('img', frame) #вывод изображения на экран пользователя

    if cv2.waitKey(1) & 0xFF == ord('q'): #если нажата клавиша "q" на клавиатуре -> выход из цикла
        break

cap.release() 
cv2.destroyAllWindows()
