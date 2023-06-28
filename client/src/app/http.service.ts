import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  header = { Authorization: `Bearer ${localStorage.getItem('token')}`}

  constructor(private http: HttpClient) { }

  get<T>(url: string) {
    return this.http.get<T>(url, { headers: this.header, observe: 'response' }).pipe(map((response:  any) => {
      const tokenFromServer = response.headers.get('Access-Token');
      if (tokenFromServer)
        localStorage.setItem('token', tokenFromServer);

      return response.body;
    }));
  }

  post<T>(url: string, payload: any) {
    return this.http.post<T>(url, payload, { headers: this.header });
  }

  delete<T>(url: string) {
    return this.http.delete<T>(url, { headers: this.header });
  }
}
