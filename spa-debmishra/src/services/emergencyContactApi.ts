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
    const response = await axios.get<Contact[]>(
      "https://debmishra.me/api/v1/emergency-contacts/data"
    );
    // Map API response keys to match the Contact interface
    const mappedContacts: Contact[] = response.data.map((contact: any) => ({
      id: contact.id,
      name: contact.name,
      mainPhone: contact["main-phone"], // Map 'main-phone' to 'mainPhone'
      secondaryPhone: contact["2nd-phone"], // Map '2nd-phone' to 'secondaryPhone'
      relation: contact.relation,
      whatsappEnabled: contact["whatsapp-on"], // Map 'whatsapp-enabled' to 'whatsappEnabled'
      comment: contact.comment,
    }));
    // console.log("Fetched contacts:", response.data);
    return mappedContacts;
  } catch (error) {
    console.error("Error fetching contacts:", error);
    return [];
  }
}
