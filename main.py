import cmd
import os
import platform
import subprocess
from gen import GenerativeAI
class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")
    
    def do_run_command(self, line):
        """Run an OS command."""
        try:
            # if platform.system() == 'Windows':
            #     command = f"cmd /c {line}"  # Use 'cmd /c' prefix for Windows commands
            # else:
            #     command = line  # For Unix-like systems, no need for prefix
            # command = line
        #     output = os.system(command)
        #     print(f"Command executed with exit code: {output}")
        # except Exception as e:
        #     print(f"Error executing command: {e}")
         # Use subprocess.run to capture output and return code
            generativeAI = GenerativeAI()
            # re = str(line)
            command = generativeAI.generate_response(line)
            print("\n"+ command +"\n")
            process = subprocess.run(command, shell=True, capture_output=True, text=True)

            if process.returncode == 0:
                print(f"Command executed successfully.\nOutput:\n{process.stdout}")
            else:
                print(f"Command failed with error: {process.stderr}")

        except Exception as e:
            print(f"Error executing command: {e}")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()