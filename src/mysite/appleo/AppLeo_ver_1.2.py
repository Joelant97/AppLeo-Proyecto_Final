# noinspection PyInterpreter
import wave
import contextlib
import speech_recognition as sr 
import tkinter 

#Main Viewer (TK): 
window = tkinter.Tk()
window.title("AppLeo ver.1.2")
window.configure(background = "black")

#Crear un Label
tkinter.Label(window, text="Bienvenido a su AppLeo_ver_1.2", bg="yellow", fg="black", font="none 12 bold").pack()
tkinter.Label(window, text='\n\n', bg="black", fg="black", font="none 12 bold").pack()

tkinter.Label(window, text="Mensaje a Leer: ", bg="yellow", fg="black", font="none 12 bold").pack()
tkinter.Label(window, text="Hola cómo estás", bg="yellow", fg="black", font="none 12 bold").pack()
tkinter.Label(window, text='\n\n', bg="black", fg="black", font="none 12 bold").pack()

def die():
    window.destroy()

#Crear un Button: 
tkinter.Button(window, text="Iniciar Prueba de Fluidez", bg="yellow", fg="black", font="none 12 bold",command=die).pack()


#Correr el Main loop
window.mainloop() 



r = sr.Recognizer()

with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)
    print ('Diga Algo!...')
    audio =r.listen (source) 
    salida = r.recognize_google(audio)
    print('Listo.\n')
    #Cuento la cantidad de palabras en la cadena
    contar = float (str(len(salida.split(" "))))

    #Salida en minusculas + guardar lo que se leera en la variable aux
    #comparar = salida.lower()
    comparar = salida
    aux = 'Hola cómo estás'


try:
    
    print('Usted Dijo:\n\n' +salida)
    print('\n')
    
    #Comparar la salida con el texto se supone a leer
    if comparar == aux: 
        print('La Lectura fue Correcta\n')

    else: 
        print('Lo que dijo y la lectura, no son iguales\n')
        print(aux)

    print("Numero de palabras: " +str(len(salida.split(" "))))
    print('\n')

    
except Exception as e:       
    print(e)                      

#Guardar la Grabacion
with open("records/grabacion.wav","wb") as f: 
    f.write(audio.get_wav_data()) 



#Calcular la duracion 
fname = 'records/grabacion.wav'

with contextlib.closing(wave.open(fname,'r')) as g:
    frames = g.getnframes()
    rate = g.getframerate()
    duracion = frames / float(rate)
    print("Tiempo Total: ")
    print(duracion,"segundos") 

    PPM = contar / duracion *60

    print('\n')
    print("Su Fluidez Lectora es de: ")
    print(PPM, "ppm") 

    tipo = int(PPM)   #Convertimos las PPM a tipo entero. 


#Validar las recomendaciones, (Recordar que esta validando niños entre 5-10 años que estan en la primaria).

try:
    print('\n')
    print('\n')
    print(" Resultados y Sugerencias: ")
    print('\n')
      
    if tipo >= 112: 
        print('Su lectura es de tipo: MUY RAPIDA\n')

    if tipo >= 100 and tipo <= 111: 
        print('Su lectura es de tipo: RAPIDA\n')

    if tipo >= 88 and tipo <= 99: 
        print('Su lectura es de tipo: MEDIANA\n')

    if tipo >= 76 and tipo <= 87: 
        print('Su lectura es de tipo: LENTA MEDIANA\n')

    if tipo >= 64 and tipo <= 75: 
        print('Su lectura es de tipo: LENTA\n')

    if tipo <= 63: 
        print('Su lectura es de tipo: MUY LENTA\n') 


except Exception as e:      
    print(e)   
