import { defineStore } from "pinia";
import { ref } from "vue";
import axios from "axios";
import router from "./router";

export const GigaStore = defineStore("GigaStore", () => {
  interface ChatMessage {
    sender: string;
    message: string;
  }

  interface LogoPass {
    username: string;
    password: string;
  }

  const server = "http://localhost:8000";
  // const server = "";

  const ChatObj = {
    typo: ref("auth"),
    secret: ref(""),
    logopass: ref<LogoPass>({
      username: "",
      password: "",
    }),
    message: ref(""),
    model: ref(""),
    spinner: ref(false),
    history: ref<ChatMessage[]>([
      { sender: "Gigachat", message: "Hello, how can I help you?" },
    ]),
    async gigachat() {
      this.spinner.value = true;
      this.history.value.push({ sender: "You", message: this.message.value });
      const element = document.getElementById("history");
      element?.scrollTo(0, 9999999999999999999999);
      const response = await axios.post(
        `${server}/gigachat/${this.typo.value}`,
        {
          model: this.model.value,
          question: this.message.value,
          auth: this.secret.value,
          login: this.logopass,
        }
      );
      const status = response.status;

      if (status === 201) {
        this.message.value = "";
        const { answer } = await response.data;
        this.history.value.push({ sender: "Gigachat", message: answer });
        element?.scrollTo(0, 9999999999999999999999);
      } else {
        router.push({ name: "auth" });
        alert("Something went wrong. Check authorization data or retry later");
      }
      this.spinner.value = false;
    },
  };

  return {
    ChatObj,
  };
});
