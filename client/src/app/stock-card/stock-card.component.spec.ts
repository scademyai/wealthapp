import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HttpClientTestingModule } from '@angular/common/http/testing';
import { StockCardComponent } from './stock-card.component';
import { HttpService } from '../http.service';

describe('StockCardComponent', () => {
  let component: StockCardComponent;
  let fixture: ComponentFixture<StockCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StockCardComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();

    fixture = TestBed.createComponent(StockCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('#addToPortfolio should call http.post', () => {
    let httpService = fixture.debugElement.injector.get(HttpService);
    spyOn(httpService, 'post').and.callThrough();
    component.addToPortfolio();
    expect(httpService.post).toHaveBeenCalled();
  });

  it('#removeFromPortfolio should call http.delete', () => {
    let httpService = fixture.debugElement.injector.get(HttpService);
    spyOn(httpService, 'delete').and.callThrough();
    component.removeFromPortfolio();
    expect(httpService.delete).toHaveBeenCalled();
  });

  it('#updateQuantity should call http.put', () => {
    let httpService = fixture.debugElement.injector.get(HttpService);
    spyOn(httpService, 'put').and.callThrough();
    component.updateQuantity(1);
    expect(httpService.put).toHaveBeenCalled();
  });
});
