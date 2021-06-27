import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '@environments/environment';
import { Session } from '@app/_models';

const baseUrl = `${environment.apiUrl}/session`;

@Injectable({ providedIn: 'root' })
export class SessionService {
    constructor(private http: HttpClient) { }

    getAll() {
        return this.http.get<Session[]>(baseUrl);
    }

    create(params: any) {
        return this.http.post(baseUrl, params);
    }
}
