import axios from "axios";

export interface Contact {
  id: number;
  name: string;
  mainPhone: string;
  secondaryPhone: string;
  relation: string;
  whatsappEnabled: string;
  comment: string;
}

export async function fetchContacts(): Promise<Contact[]> {
  try {
    const response = await axios.get<Contact[]>("http://localhost:8000/data");
    console.log("Fetched contacts:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error fetching contacts:", error);
    return [];
  }
}
