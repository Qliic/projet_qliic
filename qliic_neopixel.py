# qliic_neopixel.py

# Classe MicroPython pour contrôler une bande ou un anneau de LEDs NeoPixel (WS2812B)

import time
import machine
import neopixel # Assurez-vous d'avoir le module neopixel.py sur votre appareil

class NEOPIXEL:
    """
    Classe pour gérer une bande ou un anneau de LEDs NeoPixel (WS2812B).
    Permet de définir des couleurs pour des pixels individuels ou pour toute la bande.
    """

    def __init__(self, pin_number, num_pixels):
        """
        Initialise le contrôleur NeoPixel.
        :param pin_number: Le numéro de la broche GPIO à laquelle la bande NeoPixel est connectée.
                           (Ex: GPIO 4 pour ESP32, GPIO 2 pour ESP8266 NodeMCU D4).
        :param num_pixels: Le nombre total de LEDs NeoPixel sur la bande/l'anneau.
        """
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        self.num_pixels = num_pixels
        
        # Initialiser l'objet NeoPixel
        # Le paramètre 'bpp' (bytes per pixel) est 3 pour RGB, 4 pour RGBW.
        # La plupart des NeoPixels sont RGB, donc bpp=3.
        self.np = neopixel.NeoPixel(self.pin, self.num_pixels, bpp=3)
        
        # Éteindre toutes les LEDs au démarrage
        self.clear()
        self.show()
        print(f"NeoPixel Controller initialisé sur GPIO {pin_number} avec {num_pixels} pixels.")

    def set_pixel_color(self, index, r, g, b):
        """
        Définit la couleur d'un pixel spécifique.
        :param index: L'index du pixel à définir (commence à 0).
        :param r: Intensité du Rouge (0-255).
        :param g: Intensité du Vert (0-255).
        :param b: Intensité du Bleu (0-255).
        """
        if 0 <= index < self.num_pixels:
            # S'assurer que les valeurs sont dans la plage 0-255
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))
            self.np[index] = (r, g, b)
        else:
            print(f"Erreur: Index de pixel {index} hors de portée (0 à {self.num_pixels-1}).")

    def set_all_pixels_color(self, r, g, b):
        """
        Définit la même couleur pour tous les pixels de la bande.
        :param r: Intensité du Rouge (0-255).
        :param g: Intensité du Vert (0-255).
        :param b: Intensité du Bleu (0-255).
        """
        # S'assurer que les valeurs sont dans la plage 0-255
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        self.np.fill((r, g, b))

    def show(self):
        """
        Met à jour la bande NeoPixel avec les couleurs définies.
        Ceci doit être appelé après avoir modifié les couleurs des pixels.
        """
        self.np.write()

    def clear(self):
        """Éteint toutes les LEDs de la bande."""
        self.np.fill((0, 0, 0))
        self.show()

    def deinit(self):
        """
        Désinitialise l'objet NeoPixel et libère la broche.
        Éteint toutes les LEDs avant de désinitialiser.
        """
        self.clear()
        # La bibliothèque neopixel n'a pas de méthode deinit() directe sur l'objet np.
        # La broche est libérée lorsque l'objet np n'est plus référencé.
        # On peut explicitement supprimer la référence pour s'assurer.
        self.np = None 
        self.pin = None
        print("NeoPixel Controller désinitialisé.")
        
    def test_neopixel():
            # Initialiser une instance de notre contrôleur NeoPixel
        my_neopixel = NEOPIXEL(0, 5)
        #my_neopixel = NEOPIXEL(4, 1)

        print("\n--- Test NeoPixel ---")

        my_neopixel.clear()
        
        try:
            for i in range(0,255,10):
                print("Allumer tous les pixels en rouge...")
                my_neopixel.set_pixel_color(1, i, 0, 0)
                my_neopixel.set_pixel_color(2, 0, i, 0)
                my_neopixel.set_pixel_color(3, 0, 0, i)
                my_neopixel.set_pixel_color(0, i, i, i)
                #my_neopixel.set_all_pixels_color(i, 0, 0)

                my_neopixel.show()
                time.sleep_ms(100)
                print(i)

        except KeyboardInterrupt:
            print("Arrêt par l'utilisateur.")
        finally:
            # Toujours s'assurer que les LEDs sont éteintes et les ressources libérées
            my_neopixel.clear()


        print("Programme terminé.")

