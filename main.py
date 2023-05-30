import time
from rzctl import RZCONTROL, MOUSE_CLICK, KEYBOARD_INPUT_TYPE

def main():
    
    dll_path = "./rzctl_lib/rzctl.dll"
    
    rzctl = RZCONTROL(dll_path)
    
    if not rzctl.init():
        print("Failed to initialize rzctl")
     
    while True:
        try:
            rzctl.mouse_move(100, 200, True)
            time.sleep(1)
            print("Left click")
            rzctl.mouse_click(MOUSE_CLICK.LEFT_DOWN)
            time.sleep(1/1000)
            rzctl.mouse_click(MOUSE_CLICK.LEFT_UP)
            time.sleep(1)
            print("Scroll wheel up")
            rzctl.mouse_click(MOUSE_CLICK.SCROLL_UP)
            time.sleep(1)
            rzctl.keyboard_input(30, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
            rzctl.keyboard_input(30, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
                
            time.sleep(1/1000) # Sleep is needed to avoid razer service overflowing, which delays all your inputs
            
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    main()