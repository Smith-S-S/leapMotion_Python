import Leap, sys, time


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']

    def on_frame(self, controller):
        frame = controller.frame()

        # Get the fingers that are extended
        extended_fingers = []
        for hand in frame.hands:
            for finger in hand.fingers:
                if finger.is_extended:
                    extended_fingers.append(self.finger_names[finger.type])

        # Display the extended fingers
        if extended_fingers:
            #print (int(extended_fingers))
            print("Fingers extended:", ", ".join(extended_fingers))
        else:
            print("No fingers extended")


def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
