<template>
  <!-- <HelloWorld
    msg="Thank you for using our product. We're glad you're with us."
  /> -->
  <noscript>
    <h5 style="color: red; font-style: italic; text-align: center">
      Please enable JavaScript to properly see the website.
    </h5>
  </noscript>
  <div id="app" class="text-center mt-5">
    <h1 class="display-4">Welcome to Deb Mishra's Emergency Contacts List</h1>
    <h4 class="mt-4">
      Below table holds the list of all Emergency contacts<br />
      that you can reach out to in case of an emergency.
    </h4>
  </div>
  <div id="emergency-contacts" class="container mt-5">
    <!-- Emergency Contacts Table -->
    <EmergencyContactsTable :contacts="contacts" />
  </div>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import { onMounted, ref } from "vue";
import EmergencyContactsTable from "./components/EmergencyContactsTable.vue";
import { fetchContacts } from "./services/emergencyContactApi.ts";

export default {
  name: "App",
  components: {
    // HelloWorld,
    EmergencyContactsTable,
  },
  setup() {
    const contacts = ref([]);

    onMounted(async () => {
      contacts.value = await fetchContacts();
    });
    return {
      contacts,
    };
  },
};
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>
