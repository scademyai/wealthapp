import { Component } from '@angular/core';
import { HttpService } from './http.service';
import { take } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'wealthapp';
  isLoggedIn = false;

  constructor(private http: HttpService) {
    if(localStorage.getItem('token')) {
      this.isLoggedIn = true;
    }
  }

  login() {
    this.http.get('/api/login').pipe(take(1)).subscribe((res) => {
      this.isLoggedIn = !!res.access_token
    });
  }

  logout() {
    localStorage.removeItem('token');
    this.isLoggedIn = false;
  }
}
