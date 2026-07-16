import time
import threading



class Scheduler:


    def __init__(self):

        self.tasks = []

        self.running = False



    def add_task(
        self,
        function,
        interval
    ):

        self.tasks.append(
            {
                "function": function,
                "interval": interval,
                "last_run": 0
            }
        )



    def start(self):

        self.running = True


        print(
            "Scheduler started."
        )


        while self.running:


            now = time.time()


            for task in self.tasks:


                if now - task["last_run"] >= task["interval"]:


                    try:

                        task["function"]()


                    except Exception as error:

                        print(
                            f"Scheduler task error: {error}"
                        )


                    task["last_run"] = now



            time.sleep(
                1
            )



    def stop(self):

        self.running = False