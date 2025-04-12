<template>
  <div class="table-responsive mt-5">
    <table class="table table-bordered table-striped">
      <thead class="thead-dark">
        <tr>
          <th>id</th>
          <th>name</th>
          <th>mainPhone</th>
          <th>secondaryPhone</th>
          <th>relation</th>
          <th>whatsappEnabled</th>
          <th>comment</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(contact, index) in contacts" :key="index">
          <td>{{ contact.id }}</td>
          <td>{{ contact.name }}</td>
          <td>{{ contact.mainPhone }}</td>
          <td>{{ contact.secondaryPhone }}</td>
          <td>{{ contact.relation }}</td>
          <td>{{ contact.whatsappEnabled }}</td>
          <td>{{ contact.comment }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "EmergencyContactsTable",
  props: {
    contacts: {
      type: Array,
      required: true,
    },
  },
  computed: {
    // Computed property to sort contacts by id in ascending order
    sortedContacts() {
      return [...this.contacts].sort((a, b) => a.id - b.id);
    },
  },
};
</script>

<style>
.table {
  margin: auto;
  width: 90%;
}
</style>
