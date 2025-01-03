class CustomUtils:
    @staticmethod
    def confirm_action(prompt):
        """
        Ask for confirmation from the user.
        PRE: None
        POST: Returns True if the user confirms with 'y', otherwise False.
        """
        user_input = input(f"[DataTool] {prompt} [y/n]: ").strip().lower()
        while user_input not in ('y', 'n'):
            user_input = input("Invalid input. Please respond with 'y' or 'n': ").strip().lower()
        return user_input == 'y'