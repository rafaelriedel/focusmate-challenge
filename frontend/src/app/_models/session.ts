import { User } from './user';

export class Session {
    id!: string;
    user!: User;
    start_datetime!: Date;
}
