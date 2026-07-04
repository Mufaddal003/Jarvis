from backend.memory import Memory
from backend.llm import LLMManager

from backend.intent.classifier import IntentClassifier
from backend.intent.intent import Intent

from backend.agent.planner import AgentPlanner
from backend.agent.executor import AgentExecutor

from utils.logger import setup_logger

logger = setup_logger()


class JarvisBrain:

    def __init__(self):

        logger.info("=" * 60)
        logger.info("Initializing Jarvis Brain...")
        logger.info("=" * 60)

        # Memory
        self.memory = Memory()

        # LLM
        self.llm = LLMManager()

        # Intent Classifier
        self.classifier = IntentClassifier()

        # AI Planner
        self.agent = AgentPlanner(self.llm)

        # Executes AI Plans
        self.executor = AgentExecutor()

        logger.info("Jarvis Brain Ready!")

    def start(self):

        logger.info("Jarvis Started Successfully")

        print("\n========================================")
        print("        JARVIS AI OS STARTED")
        print("========================================")

        while True:

            try:

                command = input("\nYou : ").strip()

                if command == "":
                    continue

                if command.lower() in ["exit", "quit"]:

                    logger.info("Shutting Down Jarvis")

                    print("\nJarvis : Goodbye Sir!")

                    break

                # -----------------------------
                # Save User Message
                # -----------------------------
                self.memory.add_user(command)

                # -----------------------------
                # Detect Intent
                # -----------------------------
                intent = self.classifier.classify(command)

                # -----------------------------
                # Normal Conversation
                # -----------------------------
                if intent == Intent.CHAT:

                    reply = self.llm.ask(
                        prompt=command,
                        history=self.memory.get()
                    )

                # -----------------------------
                # AI Agent
                # -----------------------------
                else:

                    logger.info(f"Intent Detected : {intent.value}")

                    plan = self.agent.create_plan(command)

                    logger.info(f"Generated Plan : {plan}")

                    reply = self.executor.execute(plan)

                # -----------------------------
                # Save Assistant Reply
                # -----------------------------
                self.memory.add_assistant(reply)

                print(f"\nJarvis : {reply}")

            except KeyboardInterrupt:

                print("\n\nJarvis : Goodbye Sir!")

                logger.info("Keyboard Interrupt")

                break

            except Exception as e:

                logger.exception(e)

                print(f"\nJarvis : Error -> {e}")