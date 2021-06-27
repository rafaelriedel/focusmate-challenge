export class User {
    id!: string;
    firstName!: string;
    lastName!: string;
    email!: string;
    active: boolean = false;
    confirmed: boolean = false;
}
